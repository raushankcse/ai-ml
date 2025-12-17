student_name="raushan"
student_category="EBC"
print(f"registered student : {student_name} by category: {student_category}")

student_full_address = "sheikhpura, bihar, india"

print(f"first word : {student_full_address[:10]}")
print(f"first word with skip: {student_full_address[:10:2]}")
print(f"last word: {student_full_address[18:]}")
print(f"last word: {student_full_address[::-1]}")



label_text="Raushan"
encode_label= label_text.encode("utf-8")
print(f"lable text: {label_text}")
print(f"encode lable: {encode_label}")
decode_lable = encode_label.decode("utf-8")
print(f"decode text : {decode_lable}")