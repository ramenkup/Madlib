vowl_list='aeiou'
consinant_list='bcdfghjklmnpqrstvwxyz'
'''
#def print_report(txt file)
this method runs through a text file line by line and sums the number of vowls, consinants, punctuation,
and white space. it then outputs them along with their percentages in a text box formatted by the
homework outline

'''
def print_report(file_name):
    vowls=0
    consinants=0
    white=0
    punc=0
    char_num=0
    counter=0
    #counter counts the characters by +1 with each char iteration of the for loop.
    #char_num does it by adding up the results of all the boolean comparisons.

    input_file= open(file_name,"r")
    for line in input_file:
        for char in line:
            counter+=1
            if char in vowl_list:
                vowls+=1
            elif char in consinant_list:
                consinants+=1
            elif char == ' ' or char == '\t' or char == '\n':
                white+=1
            else:
                punc+=1
    char_num= vowls+consinants+white+punc
    print('----------------'+ file_name + '----------------')
    print(str('Vowls:').ljust(20)+str(vowls).rjust(5))
    print(str('Consinants:').ljust(20)+str(consinants).rjust(5))
    print(str('Whitespace:').ljust(20)+str(white).rjust(5))
    print(str('Punctuation:').ljust(20)+str(punc).rjust(5))
    print('-------------------------------------------')
    print(str('Total:').ljust(20)+str(counter).rjust(5))
    print(str('Percent vowls:').ljust(20)+ str(round((vowls / char_num)*100,1)).rjust(5))
    print(str('Percent consinants:').ljust(20) + str(round((consinants / counter)*100,1)).rjust(5))
    print(str('Percent spaces:').ljust(20) + str(round((white/counter)*100,1)).rjust(5))
    print(str('Percent punctuation:').ljust(20) + str(round((punc/ counter)*100,1)).rjust(5))
    print('=========================')

'''

def replace_parts_of_speech(string, string):

    This method is the brains of the mad lib game. given a un libbed string and the part of speech,
    The method searchs the string to find every occourance of the part of speech, and replace it with
    the word input by the user
'''
def replace_parts_of_speech(phrase, label):
    label_length= len(label)
    phrase_index=phrase.find(label)
    while phrase_index !=-1:
        phrase=phrase.replace(label, input('Enter '+label+':'), 1)
        phrase_index=phrase.find(label)#will this work, iterate to next phrase
    return phrase

'''
def complete_mad_lib(file)

    this method is the outline of the madlib game, referencing a local madlib file template, it
    writes and reads line by line each type of speech the user would need to input for the particular
    peice. It takes care to close the writer file
'''

def complete_mad_lib(lib_name):
    reader= open(lib_name)
    writer= open('Mad_'+lib_name, 'w')
    for line in reader:
        temp_line=''
        temp_line=replace_parts_of_speech(line, 'PLURAL NOUN')
        temp_line=replace_parts_of_speech(temp_line,'VERB PAST')
        temp_line=replace_parts_of_speech(temp_line,'VERB')
        temp_line=replace_parts_of_speech(temp_line,'NOUN')
        temp_line=replace_parts_of_speech(temp_line,'ADJECTIVE')
        writer.write(temp_line+'\n')
    writer.close()
    
'''
main prompts the user for an original file, runs the report, then completes the mad lib game.
'''
def main():
    mad_lib_file= input('please enter local file name:')
    print_report(mad_lib_file)
    complete_mad_lib(mad_lib_file)

if __name__ == '__main__':
    main()