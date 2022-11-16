import cv2
import argparse
from pose_results import *
import mediapipe as mp
from body_part_angle import BodyPartAngle
from exercise_types import TypeOfExercise


ap = argparse.ArgumentParser()
ap.add_argument('-t', '--exercise_type', type=str,
                help='운동 종류 선택', required=True)

ap.add_argument('-vs', '--video_source', type=str,
                help='운동 종류 선택(비디오)', required=False)

args = vars(ap.parse_args())
args = vars(ap.parse_args())

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

if args['video_source'] is not None:
    cap = cv2.VideoCapture('Exercise_videos/' + args['video_source'])
else:
    cap = cv2.VideoCapture(0)

cap.set(3, 800)  # width
cap.set(4, 480)  # height

# setup mediapipe
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:

    counter = 0
    status = True
    while cap.isOpened():
        ret, frame = cap.read()
        frame = cv2.resize(frame, (800, 480), interpolation=cv2.INTER_AREA)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame.flags.writeable = False

        results = pose.process(frame)
        frame.flags.writeable = True
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        try:
            landmarks = results.pose_landmarks.landmark
            counter, status = TypeOfExercise(landmarks).calculate_exercise(
                args['exercise_type'], counter, status)

        except:
            pass

        frame = score_table(args['exercise_type'], frame, counter, status)

        # render detections
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=2))
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(175, 139, 45), thickness=2, circle_radius=2))

        cv2.imshow('Video', frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
