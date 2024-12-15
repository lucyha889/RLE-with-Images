import console_gfx

# Function to display the menu
def display_menu():
    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image:")
    console_gfx.display_image(console_gfx.test_rainbow)
    print("\n\nRLE Menu")
    print("--------")
    print("0. Exit")
    print("1. Load File")
    print("2. Load Test Image")
    print("3. Read RLE String")
    print("4. Read RLE Hex String")
    print("5. Read Data Hex String")
    print("6. Display Image")
    print("7. Display RLE String")
    print("8. Display Hex RLE Data")
    print("9. Display Hex Flat Data\n")

# Utility function to convert a list of numbers < 16 to a hexadecimal string
def to_hex_string(data): #data is a list of numbers <16
    s1 =""
    for i in data:
        s1+=hex(i).split("x")[1]  #0xF -> get string right of x or hex(i).split("x")[-1] -1 last string
    return s1

def count_runs(flat_data): #flat_data is a list of numbers <16
    runs = 1
    length_in_run=0 
    num1 = flat_data[0] #first number in flat_data
    for i in flat_data:
        if i == num1:
            length_in_run+=1 #count the length of the run
            if length_in_run==16:
                runs+=1
                length_in_run=1
        else:
            runs+=1 
            num1 = i
            length_in_run=1
           
    return runs

def encode_rle(flat_data): 
    num1 = flat_data[0]
    rel = []
    length_in_run=0
    for i in flat_data: 
        if i == num1:
            length_in_run+=1
            if length_in_run==16: #if length_in_run==16, add the run to rel and reset length_in_run
                rel.extend([length_in_run-1, i]) #length_in_run-1 because length_in_run is already 1
                length_in_run=1
        else:
            rel.extend([length_in_run, num1]) #add the run to rel
            num1 = i
            length_in_run=1
    rel.extend([length_in_run, num1])
    return rel

def get_decoded_length(rle_data):
    length=0
    for i in rle_data[::2]:  #some_list[start:stop:step]
        length+=i
    return length

def decode_rle(rle_data):
    flat_data=[] 
    i=0
    for ele in rle_data[::2]:  #some_list[start:stop:step, loop the odd numbers
        flat_data.extend((ele*[rle_data[1::2][i]]))   # loop the even numbers, repeat ele times
        i+=1
    return flat_data

def string_to_data(data_string):
    data=[]
    lst = list(data_string) #break string to charactor list
    for ele in lst:
        a=int(ele, 16)
        data.append(a)
    return data

def to_rle_string(rle_data):
    s1=""
    list0=rle_data[::2]
    list1=rle_data[1::2]
    for i in range(len(rle_data[::2])):
        #s1+=hex(rle_data[::2][i]).split("x")[-1]+hex(rle_data[1::2][i]).split("x")[-1]+":"
        s1+=str(rle_data[::2][i])+hex(rle_data[1::2][i]).split("x")[-1]+":"
    s1=s1[:-1] #remove the last unnecessary :
    return s1 

def string_to_rle(rle_string):
    lst =rle_string.split(":") #split the string and get rid of :
    rle_data = []
    for ele in lst:
        rle_data.append(int(ele[:-1]))
        rle_data.append(int(ele[-1:],16))
    return rle_data
