All the codes are named according to the date I wrote the code
All the codes (except codes in folder "rider") are written based on the data structure in the folder "data"

folder "correct_volume" contains files with the actual volumes of the tumor instead of voxel volume
folder "rider" contains files that compare data with contrast vs. data without contrast

**dicom_header.py** extracts headers from CT scans. It reads the first CT scan in each folder. You could change the parameter extracted by changing the list "extracted_info". 
**combine_data.py** combines data from csv files located under each patients' folder to one single csv. 
**combat.py** uses the output of **combine_data.py** and apply ComBat according to the batch specify. 
**volume_combat.py** plots post-ComBat data vs. voxel volume. 
**combat_original.py** plots both post-ComBat and pre-ComBat data vs. voxel volume. 
**both_line.py** plots both post-ComBat and pre-ComBat data vs. voxel volume and save R-square values into a csv file. 
**combat_rider.py** plots both post-ComBat and RIDER data vs. voxel volume. 
**histogram.py** plots data for each feature into a histogram. 
**whisker.py** plots whisker and box diagrams for both post-ComBat and pre-ComBat data for each batch. Each graph shows one feature. 
**calculate_pixelspacing.py** calculate the pixel spacings for each CT and ave the results into a csv file. 
**aorta_combat.py** similar to **combat.py**
**patient_144.py** remove all the patients not included in ComBat and features cannot be plotted. 
