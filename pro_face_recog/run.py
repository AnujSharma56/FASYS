import face_recognition
import cv2
import numpy as np
import os
import sys
import pandas as pd
import json
import argparse
import time

from datetime import datetime

#for testing purpose
parser = argparse.ArgumentParser(description="Face Recognition")
parser.add_argument("--scan", "-s", type=str, help="Start scanning faces from pre-trained data")
parser.add_argument("--train", "-t", type=str, help="Train data and store to given file")

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)


def train(train_file):
    print("Training data")
    # Create arrays of known face encodings and their names
    train_data = {}
    # Load pics from data folder and recognise them
    for pic in os.listdir("pro_face_recog/data"):
        if (pic.split(".")[-1].lower() == "jpg") or (pic.split(".")[-1].lower() == "png"):
            temp_image = face_recognition.load_image_file("pro_face_recog/data/"+pic)
            #temp_image = face_recognition.load_image_file("data/"+pic)
            name = pic.split(".")[0]
            try:
                temp_image_encoding = face_recognition.face_encodings(temp_image)[0].tolist()
                if name in train_data.keys():
                    train_data[name] = train_data[name].append(temp_image_encoding)
                else:
                    train_data[name] = [temp_image_encoding]

            except Exception as e:
                print(f"Problem in - {pic}")
    
    print("Storing to file")
    with open(train_file, "w") as train_dump:
        json.dump(train_data, train_dump)

def event(action):
    if action % 5 == 0:
        return True
    else:
        return False

def scan_faces(known_face_encodings, known_face_names,t=10):

    print("Started scanning")

    # Minutes to run for
    mins = t
    end_time = time.time() + 60 * mins

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    df = pd.DataFrame({'name':[], 'timestamp':[]})
    print(df)
    action = 0
    while time.time() < end_time:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown User"

                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                if name not in face_names:
                    face_names.append(name)
        
        if event(action):
            print("Appending to DF")
            for name in face_names:
                df = df.append({
                    "name": name,
                    "timestamp": datetime.now()
                }, ignore_index=True)
        
        action += 1

        process_this_frame = not process_this_frame

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    print(df)
    
    store_latest_values(df)

def store_latest_values(df, threshold=6):
    with open("result.csv", "w") as result:
        df.to_csv("result.csv", index=False, header=True)
    grouped = df.groupby('name').count()
    grouped = grouped.reset_index()
    filter_list = list(grouped[grouped['timestamp'].apply(lambda x: x>threshold)]['name'])
    df = df[df['name'].apply(lambda x: x in filter_list)].groupby('name').tail(1).sort_values('timestamp', ascending=False)
    df.to_csv('latest.csv', index=False)


def load_train_data(train_file):

    train_data = json.load(open(train_file))

    known_face_names = [name for name in train_data.keys() for i in range(len(train_data[name]))]
    known_face_encodings = [np.array(enc) for res in train_data.values() for enc in res]

    return known_face_encodings, known_face_names

def main():

    args = None

    try:
        args = vars(parser.parse_args(sys.argv[1:]))
        print("Arguments parsed.")
    except:
        parser.print_help()
        sys.exit()

    if args['scan']:
        kfe, kfn = load_train_data(args['scan'])
        scan_faces(kfe, kfn)
    elif args['train']:
        train(args['train'])

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
