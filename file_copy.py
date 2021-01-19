## 15.Write a program, to create a text file SOURCE.TXT and 
# write some lines to it and copy to another file named as TARGET.TXT 
# by converting each of the alphabets to upper case letter.

def main():
    ori_file = open("SOURCE.TXT","w+")
    dummy_text = ["Hello", "\nWorld", "\npeace", "\nAlwaYS"]
    ori_file.writelines(dummy_text)
    ori_file.seek(0)
    ##copying to another file with all alphabets upper case
    target_file = open("TARGET.TXT","w+")
    for line in ori_file:
        target_file.write(line.upper())
    
    target_file.seek(0)
    print(f"{target_file.read()}")
    ori_file.close()
    target_file.close()

main()