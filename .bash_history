cd
sudo apt-get update
sudo apt-get install -y cmake git g++ libtool
sudo apt-get install -y libleptonica-dev
sudo apt-get install -y libarchive-dev libpng-dev libjpeg-dev libwebp-dev libtiff5-dev libicu-dev
cd tesssudo apt-get install -y cmake git g++ libtool
sudo apt-get install -y cmake git g++ libtool
sudo apt-get install -y libleptonica-dev
sudo apt-get install -y libarchive-dev libpng-dev libjpeg-dev libwebp-dev libtiff5-dev libicu-dev
sudo apt-get install -y libicu-dev libpango1.0-dev libcairo2-dev
./autogen.sh
./configure --enable-training
cd tesseract
cdgit clone https://github.com/tesseract-ocr/tesseract.git
git clone https://github.com/tesseract-ocr/tesseract.git
cd tesseract
./autogen.sh
./configure --enable-training
make
sudo make install
sudo ldconfig
make training
sudo make training-install
tesseract --version
tesseract --list-langs
cd ..
cd usr/local/share/tessdata/
wget https://github.com/tesseract-ocr/tessdata_best/raw/main/ara.traineddata
tesseract --list-langs
cd
tesseract
cd tesseract
cd tessdata
ls
wget https://github.com/tesseract-ocr/tessdata_best/raw/main/ara.traineddata
sudo mv ara.traineddata /usr/local/share/tessdata/
tesseract --list-langs
cd
git clone https://github.com/tesseract-ocr/tesstrain.git
cd tesstrain/
make tesseract-langdata
mkdir -p usr/share/tessdata
mkdir - usr/share/tessdata
mk dir usr/share/tessdata
mkdir usr/share/tessdata
cd
sudo apt-get install python3 python3-pip
pip install Pillow>=6.2.1 python-bidi>=0.4 matplotlib pandas
pip install Pillow>=6.2.1
pip install Pillow python-bidi matplotlib pandas
cd tesstrain
make training MODEL_NAME=tst START_MODEL=ara
tesseract --list-langs
sudo mv eng.traineddata /usr/local/share/tessdata/
make training MODEL_NAME=tst START_MODEL=ara
sudo apt-get install bc
make training MODEL_NAME=tst START_MODEL=ara
cd
nano eval_ocr.sh
chmod +x eval_ocr.sh 
combine_tessdata -e tesseract/tessdata/ara.traineddata ara.lstm
cd tesseract
cd
combine_tessdata -e tesseract/tessdata/ara.traineddata ara.lstm
combine_tessdata -e home/ocr_project/tesseract/tessdata/ara.traineddata ara.lstm
combine_tessdata -e tesseract/tessdata/ara.traineddata ara.lstm
./eval_ocr.sh 
nano eval_ocr.sh 
./eval_ocr.sh 
nano eval_ocr.sh 
./eval_ocr.sh 
nano eval_ocr.sh 
./eval_ocr.sh 
nano eval_ocr.sh 
./eval_ocr.sh 
nano eval_ocr.sh 
./eval_ocr.sh 
nano eval_ocr.sh 
./eval_ocr.sh 
nano eval_ocr.sh 
./eval_ocr.sh 
nano eval_ocr.sh 
./eval_ocr.sh 
nano eval_ocr.sh 
./eval_ocr.sh 
nano eval_ocr.sh 
./eval_ocr.sh 
nano eval_ocr.sh 
./eval_ocr.sh 
nano eval_ocr.sh 
./eval_ocr.sh 
nano eval_ocr.sh 
./eval_ocr.sh 
nano eval_ocr.sh 
./eval_ocr.sh 
nano reverse_text.sh
chmod +x reverse_text.sh 
./reverse_text.sh 
nano eval_ocr.sh 
./eval_ocr.sh 
nano eval_ocr.sh 
cd
./eval_ocr.sh 
cd tesstrain/
make training MODEL_NAME=evaluation_folder_copy START_MODEL=ara
cd ..
./eval_ocr.sh 
nano reverse_text.sh 
./reverse_text.sh 
nano reverse_text.sh 
./reverse_text.sh 
nano reverse_text.sh 
./reverse_text.sh 
nano reverse_text.sh 
./reverse_text.sh 
nano reverse_text.sh 
./reverse_text.sh 
nano reverse_text.sh 
./reverse_text.sh 
make training MODEL_NAME=evaluation_folder_copy START_MODEL=ara
cd tesstrain/
make training MODEL_NAME=evaluation_folder_copy START_MODEL=ara
cd
./eval_ocr.sh 
nano eval_ocr.sh 
./eval_ocr.sh 
combine_tessdata -e ara_model_1.traineddata ara_model_1.lstm
nano eval_ocr.sh 
./eval_ocr.sh 
nano eval_ocr.sh 
./eval_ocr.sh 
cd tesstrain
make training MODEL_NAME=correct START_MODEL=ara MAX_ITERATIONS=10000
make training MODEL_NAME=correct START_MODEL=ara MAX_ITERATIONS=500
nano eval_ocr.sh 
./eval_ocr.sh 
nano eval_ocr.sh 
./eval_ocr.sh 
nano eval_ocr.sh 
./eval_ocr.sh 
nano generate_text.py
python generate_text.py 
python3 generate_text.py 
nano generate_text.py
python3 generate_text.py 
nano split_training_text.py
python3 split_training_text.py 
nano split_training_text.py
python3 split_training_text.py 
nano split_training_text.py
python3 split_training_text.py 
nano split_training_text.py
python3 split_training_text.py 
cd tesstrain
make training MODEL_NAME=random START_MODEL=ara MAX_ITERATIONS=10000
cd ..
nano split_training_text.py
python3 split_training_text.py 
nano split_training_text.py
python3 split_training_text.py 
cd tess
cd tesstrain/
make training MODEL_NAME=random START_MODEL=ara MAX_ITERATIONS=10000
cd
nano eval_ocr.sh 
./eval_ocr.sh 
cd
./eval_ocr.sh \
./eval_ocr.sh 
nano eval_ocr.sh 
./eval_ocr.sh 
nano eval_ocr.sh 
./eval_ocr.sh 
cd
./eval_ocr.sh 
nano eval_ocr.sh 
./eval_ocr.sh 
cd tesstrain
cd make
ls
cd Makefile
explorer.exe Makefile
cd tessdata
cd data
ls
rmdir ara
rm ara
cd ..
make training MODEL_NAME=random START_MODEL=ara MAX_ITERATIONS=2000
make training MODEL_NAME=random START_MODEL=ara MAX_ITERATIONS=10000
cd ..
./eval_ocr.sh 
nano generate_text.py
python3 generate_text.py 
nano split_training_text.py
python3 split_training_text.py 
cd tesstrain/
make training MODEL_NAME=random START_MODEL=ara MAX_ITERATIONS=100000
cd
ls
./eval_ocr.sh 
cd tesstrain/
make training MODEL_NAME=random START_MODEL=ara MAX_ITERATIONS=100000
cd ..
./eval_ocr.sh 
cdd
cd
nano generate_text.py 
python3 generate_text.py 
nano split_training_text.py
python3 split_training_text.py 
nano split_training_text.py
nano generate_text.py 
python3 generate_text.py 
python3 split_training_text.py 
cd
cd tesstrain
make training MODEL_NAME=dejavu START_MODEL=ara MAX_ITERATIONS=10000
cd
nano split_training_text.py
python3 split_training_text.py 
cd tesstrain/
make training MODEL_NAME=dejavu START_MODEL=ara MAX_ITERATIONS=10000
cd
nano eval_ocr.sh 
./eval_ocr.sh 
cd
./eval_ocr.sh 
nano eval_ocr.sh 
./eval_ocr.sh 
cd
pythonon3 split_training_text.py
python3 split_training_text.py 
cd tesstrian
cd tesstrain/
make training MODEL_NAME=dejavu START_MODEL=ara MAX_ITERATIONS=10000
cd
nano eval_ocr.sh 
./eval_ocr.sh 
cd
cd tesstrain/
make training MODEL_NAME=moheb START_MODEL=ara MAX_ITERATIONS=20000
cd
nano eval_ocr.sh 
./eval_ocr.sh 
nano eval_ocr.sh 
cd
./eval_ocr.sh 
cd tesstrain/
make training MODEL_NAME=moheb START_MODEL=ara MAX_ITERATIONS=2
cd
./eval_ocr.sh 
cd tesstrain/
make training MODEL_NAME=moheb START_MODEL=ara MAX_ITERATIONS=500000
cat /proc/self/fd/0
cat /proc/self/fd/0 | less
fc-list
fc-list :lang=ar
cd tesstrain/
make training MODEL_NAME=moheb START_MODEL=ara MAX_ITERATIONS=500000
cd tesstrain/
make training MODEL_NAME=moheb START_MODEL=ara MAX_ITERATIONS=500000
cd
nano eval_ocr.sh 
./eval_ocr.sh 
nano generate_text.py 
python3 generate_text.py 
nan split_training_text.py
nano split_training_text.py
python3 split_training_text.py 
nano eval_ocr.sh 
cd tesstrain/
make training MODEL_NAME=dejavu START_MODEL=ara MAX_ITERATIONS=5
cd
./eval_ocr.sh 
sudo apt update
sudo apt install fonts-arabeyes
fc-list :lang=ar
nano split_training_text.py
python3 split_training_text.py 
nano split_training_text.py
fc-list :lang=ar
nano split_training_text.py
python3 split_training_text.py 
nano split_training_text.py
python3 split_training_text.py 
fc-list :lang=ar
cd tesstrain/
make training MODEL_NAME=dejavu START_MODEL=ara MAX_ITERATIONS=100000
cd
nano eval_ocr.sh 
./eval_ocr.sh 
cd
./eval_ocr.sh 
nano eval_ocr.sh 
nano generate_text.py 
python3 generate_text.py 
nano split_training_text.py
python3 split_training_text.py 
nano split_training_text.py
python3 split_training_text.py 
cd tesstrain/
make training MODEL_NAME=synth START_MODEL=ara MAX_ITERATIONS=100000
cd
nano eval_ocr.sh 
./eval_ocr.sh 
nano eval_ocr.sh 
./eval_ocr.sh 
cd
nano generate_text.py 
cd
python3 generate_text.py 
fc-list :lang=ar
cd
nano split
nano split_training_text.py
python3 split_training_text.py 
cd
python3 split_training_text.py 
python3 generate_text.py 
python3 split_training_text.py 
python3 split_training_text.py 
cd tesstrain
make training MODEL_NAME=no_error START_MODEL=ara MAX_ITERATIONS=500000
nano create_error.py
حصي
pwd
python3 create_error.py 
nano delete_lstmf_files.py
python3 delete_lstmf_files.py 
nano delete_lstmf_files.py
python3 delete_lstmf_files.py 
python3 create_error.py 
cd tesstrain/
make training MODEL_NAME=ten_char_error START_MODEL=ara MAX_ITERATIONS=12800
make training MODEL_NAME=ten_char_error START_MODEL=ara MAX_ITERATIONS=34000
cd
python3 create_error.py 
cd tesstrain/
make training MODEL_NAME=twenty_char_error START_MODEL=ara MAX_ITERATIONS=12800
make training MODEL_NAME=twenty_char_error START_MODEL=ara MAX_ITERATIONS=34000
make training MODEL_NAME=trying START_MODEL=ara MAX_ITERATIONS=12800
cd tesstrain/
make training MODEL_NAME=trying START_MODEL=ara MAX_ITERATIONS=12800
python3 split_training_text.py 
cd tesstrain
make training MODEL_NAME=trying START_MODEL=ara MAX_ITERATIONS=40000
cd
./reverse_text.sh 
cd tesstrain/
make training MODEL_NAME=trying START_MODEL=ara MAX_ITERATIONS=40000
cd
./reverse_text.sh 
cd tesstrain/
make training MODEL_NAME=trying START_MODEL=ara MAX_ITERATIONS=40000
python3 create_error.py 
python3 split_training_text.py 
python3 create_error.py 
cd tesstrain
make training MODEL_NAME=trying START_MODEL=ara MAX_ITERATIONS=40000
cd
python3 split_training_text.py 
python3 create_error.py 
python3 split_training_text.py 
python3 create_error.py 
python3 split_training_text.py 
cd tesstrain/
make training MODEL_NAME=trying START_MODEL=ara MAX_ITERATIONS=40000
cd
python3 create_error.py 
cd tesstrain/
make training MODEL_NAME=trying START_MODEL=ara MAX_ITERATIONS=40000
cd
python3 split_training_text.py 
python3 create_error.py 
cd tesstrain/
make training MODEL_NAME=trying START_MODEL=ara MAX_ITERATIONS=40000
cd
python3 split_training_text.py 
python3 create_error.py 
python3 split_training_text.py 
python3 create_error.py 
python3 split_training_text.py 
python3 create_error.py 
python3 split_training_text.py 
python3 create_error.py 
python3 split_training_text.py 
python3 create_error.py 
python3 split_training_text.py 
python3 create_error.py 
python3 split_training_text.py 
cd tesstrain/
make training MODEL_NAME=trying START_MODEL=ara MAX_ITERATIONS=40000
python3 split_training_text.py 
python3 split_training_text.py 
python3 split_training_text.py 
python3 split_training_text.py 
cd
python3 split_training_text.py 
cd tesstrain/
make training MODEL_NAME=evaluation START_MODEL=ara MAX_ITERATIONS=25000
cd
python3 generate_text.py 
python3 split_training_text.py 
./eval_ocr.sh 
cd
python3 create_error.py 
python3 split_training_text.py 
python3 create_error.py 
python3 split_training_text.py 
python3 generate_text.py 
cd tesstrain/
make training MODEL_NAME=no_error START_MODEL=ara MAX_ITERATIONS=25000
cd
python3 create_error.py 
python3 split_training_text.py 
cd tesstrain/
make training MODEL_NAME=eval_data START_MODEL=ara MAX_ITERATIONS=25000
cd
./eval_ocr.sh 
cd
./reverse_text.sh 
./eval_ocr.sh 
cd tesstrain/
make training MODEL_NAME=eval_data START_MODEL=ara MAX_ITERATIONS=25000
cd
./eval_ocr.sh 
cd
python3 create_error.py 
python3 split_training_text.py 
python3 create_error.py 
python3 split_training_text.py 
cd tesstrain/
make training MODEL_NAME=twenty_char_error START_MODEL=ara MAX_ITERATIONS=25000
cd tesstrain/
make training MODEL_NAME=fifteen_char_error START_MODEL=ara MAX_ITERATIONS=25000
cd tesstrain/
make training MODEL_NAME=no_error START_MODEL=ara MAX_ITERATIONS=34000
make training MODEL_NAME=ten_char_error START_MODEL=ara MAX_ITERATIONS=25000
cd
./eval_ocr.sh 
python3 create_error.py 
python3 split_training_text.py 
make training MODEL_NAME=no_error START_MODEL=ara MAX_ITERATIONS=25000
cd tesstrain/
make training MODEL_NAME=no_error START_MODEL=ara MAX_ITERATIONS=25000
cd
cd tesstrain
make training MODEL_NAME=twenty_five_char_error START_MODEL=ara MAX_ITERATIONS=25000
cd
nano vocalize.py
python3 vocalize.py 
nano vocalize.py
python3 vocalize.py 
nano vocalize.py
python3 vocalize.py 
nano create_vocal_error.py
python3 create_vocal_error.py 
nano create_vocal_error.py
python3 create_vocal_error.py 
nano create_vocal_error.py
python3 create_vocal_error.py 
cd tesstrai
cd tesstrain/
make training MODEL_NAME=five_char_error START_MODEL=ara MAX_ITERATIONS=25000
make training MODEL_NAME=high_vocalized_no_error START_MODEL=ara MAX_ITERATIONS=25000
cd tesstrain/
make training MODEL_NAME=high_vocalized_no_error START_MODEL=ara MAX_ITERATIONS=25000
make training MODEL_NAME=low_vocalized_no_error START_MODEL=ara MAX_ITERATIONS=25000
cd
python3 split_training_text.py 
cd
nano create_similar_char_error.py
cd
nano create_similar_char_error.py 
cd
python3 create_similar_char_error.py 
python3 split_training_text.py 
cd tesstrain
make training MODEL_NAME=fifteen_char_error START_MODEL=ara MAX_ITERATIONS=25000
cd tesstrain/
make training MODEL_NAME=twenty_five_char_error START_MODEL=ara MAX_ITERATIONS=25000
cd tesstrain/
make training MODEL_NAME=fifteen_char_error START_MODEL=ara MAX_ITERATIONS=25000
cd tesstrain/
make training MODEL_NAME=fifteen_char_error START_MODEL=ara MAX_ITERATIONS=25000
make training MODEL_NAME=twenty_five_char_error START_MODEL=ara MAX_ITERATIONS=25000
cd
python3 create_similar_char_error.py 
cd
./eval_ocr.sh 
cd tesstrain/
make training MODEL_NAME=mid_vocalized_no_error START_MODEL=ara MAX_ITERATIONS=25000
cd tesstrain/
make training MODEL_NAME=five_char_error START_MODEL=ara MAX_ITERATIONS=25000
cd tesstrain/
make training MODEL_NAME=mid_vocalized_no_error START_MODEL=ara MAX_ITERATIONS=25000
cd
python3 split_training_text.py 
cd tesstrain/
make training MODEL_NAME=fifteen_similar_char_error START_MODEL=ara MAX_ITERATIONS=25000
cd tesstrain/
make training MODEL_NAME=fifteen_similar_char_error START_MODEL=ara MAX_ITERATIONS=25000
cd tesstrain/
make training MODEL_NAME=ten_similar_char_error START_MODEL=ara MAX_ITERATIONS=25000
make training MODEL_NAME=twenty_similar_char_error START_MODEL=ara MAX_ITERATIONS=25000
cd tesstrain/
make training MODEL_NAME=five_similar_char_error START_MODEL=ara MAX_ITERATIONS=25000
cd tesstrain/
make training MODEL_NAME=twenty_five_similar_char_error START_MODEL=ara MAX_ITERATIONS=25000
cd tesstrain/
make training MODEL_NAME=five_similar_char_error START_MODEL=ara MAX_ITERATIONS=25000
cd tesstrain/
make training MODEL_NAME=high_vocalized_error START_MODEL=ara MAX_ITERATIONS=25000
cd tesstrain/
make training MODEL_NAME=low_vocalized_error START_MODEL=ara MAX_ITERATIONS=25000
cd tesstrain/
make training MODEL_NAME=mid_vocalized_error START_MODEL=ara MAX_ITERATIONS=25000
cd
cd tesstrain/
make training MODEL_NAME=low_vocalized_no_error START_MODEL=ara MAX_ITERATIONS=25000
make training MODEL_NAME=low_vocalized_no_error START_MODEL=ara MAX_ITERATIONS=35000
cd
python3 create_omit_error.py 
cd
python3 split_training_text.py 
cd
python3 split_training_text.py 
cd tesstrain/
make training MODEL_NAME=low_vocalized_no_error START_MODEL=ara MAX_ITERATIONS=25000
make training MODEL_NAME=low_vocalized_no_error START_MODEL=ara MAX_ITERATIONS=250000
make training MODEL_NAME=low_vocalized_no_error START_MODEL=ara MAX_ITERATIONS=100000
make training MODEL_NAME=mid_vocalized_no_error START_MODEL=ara MAX_ITERATIONS=100000
cd tesstrain/
make training MODEL_NAME=twenty_five_char_omit_error START_MODEL=ara MAX_ITERATIONS=25000
cd tesstrain/
make training MODEL_NAME=low_vocalized_no_error START_MODEL=ara MAX_ITERATIONS=100000
make training MODEL_NAME=mid_vocalized_no_error START_MODEL=ara MAX_ITERATIONS=100000
make training MODEL_NAME=high_vocalized_no_error START_MODEL=ara MAX_ITERATIONS=100000
cd
cd tesstrain
make training MODEL_NAME=high_vocalized_no_error START_MODEL=ara MAX_ITERATIONS=25000
make training MODEL_NAME=high_vocalized_no_error START_MODEL=ara MAX_ITERATIONS=100000
make training MODEL_NAME=mid_vocalized_no_error START_MODEL=ara MAX_ITERATIONS=100000
make training MODEL_NAME=low_vocalized_no_error START_MODEL=ara MAX_ITERATIONS=100000
make training MODEL_NAME=twenty_char_omit_error START_MODEL=ara MAX_ITERATIONS=25000
make training MODEL_NAME=fifteen_char_omit_error START_MODEL=ara MAX_ITERATIONS=25000
make training MODEL_NAME=ten_char_omit_error START_MODEL=ara MAX_ITERATIONS=25000
make training MODEL_NAME=five_char_omit_error START_MODEL=ara MAX_ITERATIONS=25000
make training MODEL_NAME=five_char_error START_MODEL=ara MAX_ITERATIONS=25000
make training MODEL_NAME=five_char_omit_error START_MODEL=ara MAX_ITERATIONS=25000
fonts --help
fc-list
python3 split_training_text.py 
pip install Pillow
cd
nano tif_to_png.py
python3 tif_to_png.py 
cd tesstrain
make training MODEL_NAME=five_char_omit_error START_MODEL=ara MAX_ITERATIONS=25000
python3 split_training_text.py 
python3 create_vocal_error.py 
python3 split_training_text.py 
make training MODEL_NAME=five_char_omit_error START_MODEL=ara MAX_ITERATIONS=25000
cd tesstrain/
make training MODEL_NAME=five_char_omit_error START_MODEL=ara MAX_ITERATIONS=25000
make training MODEL_NAME=low_vocalized_error START_MODEL=ara MAX_ITERATIONS=100000
cd tesstrain/
make training MODEL_NAME=low_vocalized_error START_MODEL=ara MAX_ITERATIONS=100000
cd tesstrain/
make training MODEL_NAME=low_vocalized_error START_MODEL=ara MAX_ITERATIONS=100000
make training MODEL_NAME=medium_vocalized_error START_MODEL=ara MAX_ITERATIONS=100000
make training MODEL_NAME=mid_vocalized_error START_MODEL=ara MAX_ITERATIONS=100000
make training MODEL_NAME=high_vocalized_error START_MODEL=ara MAX_ITERATIONS=100000
cd
cd tesstrian
cd tesstrain/
make training MODEL_NAME=twenty_five_char_omit_error START_MODEL=ara MAX_ITERATIONS=25000
./eval_ocr.sh 
python3 vocalize.py 
python3 split_training_text.py 
./eval_ocr.sh 
cd tesstrain/
make training MODEL_NAME=high_diacritics_evaluation START_MODEL=ara MAX_ITERATIONS=25000
make training MODEL_NAME=mid_diacritics_evaluation START_MODEL=ara MAX_ITERATIONS=25000
make training MODEL_NAME=low_diacritics_evaluation START_MODEL=ara MAX_ITERATIONS=25000
cd
./eval_ocr.sh 
su ocr_project
cd
git add .
cd
git init
git add .
git commit -m "project"
git config --global user.email "ahmedelshafie60@gmail.com"
git commit -m "project"
git config --global user.email "ahmedelshafie60@gmail.com"
git config --global user.name "ahmede60"
git login
git commit -m "project"
git remote add origin https://github.com/ahmede60/ocr_project
git push -u origin master
git remote add origin https://github.com/ahmede60/ocr_project
git push -u origin master
git login
git config --global user.email "ahmedelshafie60@gmail.com"
git config --global user.name "ahmede60"
git push -u origin master
git help
git remote add origin https://github.com/ahmede60/ocr_project.git
git push
git push --set-upstream origin master
git remote add origin git@github.com:ahmede60/ocr_project.git
git push --set-upstream origin master
git remote add origin https://github.com/ahmede60/ocr_project.git
git init
git add .
git commit -m "project"
git remote set-url origin https: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@github.com/ahmede60/ocr_project.git
git remote add origin https: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@github.com/ahmede60/ocr_project.git
git push --set-upstream origin master
git remote set-url origin https://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@github.com/ahmede60/ocr_project.git
git push --set-upstream origin master
git remote set-url origin https://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@github.com/ahmede60/ocr_project.git
git push --set-upstream origin master
su ocr_project
