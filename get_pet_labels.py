#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def format_names(names):
    lable = str(names)
    lable_lower = lable.lower()
    lable_list = lable_lower.split("_")
    #print(lable_list[0])
    empty_lable = ""
    for x in range(0,len(lable_list)):
        if lable_list[x].isalpha():
            empty_lable += lable_list[x] + " "
    
    final_lable = empty_lable.strip()
    return final_lable

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    file_names = listdir(image_dir)
    result_dic = dict()
    pet_lables = []
    #items_in_dic = len(results_dic)
    
    """for idx in range(0, len(file_names)):
       if format_names(file_names[idx]) not in pet_lables:
           # result_dic[filenames[idx]
        pet_lables.append(format_names(file_names[idx]))"""
    
    for idx in range(0,len(file_names)):
        pet_lables.append(format_names(file_names[idx]))
        if file_names[idx] not in result_dic:
            result_dic[file_names[idx]] = pet_lables[idx]
        else:
            print("Warning: Key=", file_names[idx], "already exists in results_dic with value =",
                   result_dic[file_name[idx]])
            
    #print(result_dic)
    
    # Replace None with the results_dic dictionary that you created with this
    # function
    return result_dic
