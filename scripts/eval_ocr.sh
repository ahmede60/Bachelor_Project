\#!/bin/bash

# Specify the folder path containing LSTM files
LSTM_FOLDER_PATH="/home/ocr_project/tesstrain/data/high_diacritics_evaluation-ground-truth"

# Specify the paths for lstmeval
# MODEL_PATH="tesstrain/data/low_vocalized_error/checkpoints/low_vocalized_error_checkpoint"
# TRAINEDDATA_PATH="tesstrain/data/low_vocalized_error.traineddata"

MODEL_PATH="ara.lstm"
TRAINEDDATA_PATH="tesseract/tessdata/ara.traineddata"

# Create a temporary file with paths to LSTM files
TEMP_FILE="/tmp/tempfile.txt"

find "$LSTM_FOLDER_PATH" -type f -name "*.lstmf" > "$TEMP_FILE"

# Run lstmeval with the generated temporary file
LC_ALL=C lstmeval --model "$MODEL_PATH" --traineddata "$TRAINEDDATA_PATH" --eval_listfile "$TEMP_FILE"

# Delete the temporary file
