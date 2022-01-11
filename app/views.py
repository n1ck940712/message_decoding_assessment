from django.http.response import JsonResponse
from django.shortcuts import render
import json

# main page
def index(request):
    data = {
        'user': request.user,
        'message': 'message',
    }
    return render(request, "index.html", data)

def decode(request):
    if request.method == 'POST':
        try:
            submit_input = json.loads(request.POST.get('submit_input'))
            header = submit_input.split('\n')[0]
            pattern = ''.join(submit_input.split('\n')[1:])
            print('header: %s' % header)
            print('pattern: %s' % pattern)
            decoded_message = decode_message(header, pattern)
        except:
            decoded_message = 'Invalid message'
    data = {
        'success': True,
        'decoded_message': decoded_message
    }
    return JsonResponse(data)



def check_segment_end(length, input):
    if input == len(input) * '1':
        return True
    else:
        return False

def get_character(input):
    binary_disp = '0'
    for i in range(1000):
        if binary_disp == len(binary_disp) * '1':
            binary_disp = (len(binary_disp)+1) * '0'
        if input == binary_disp:
            return i
        binary_disp = str(bin(int(binary_disp, 2) + 1)[2:]).rjust(len(binary_disp), '0')
    return 

def decode_message(header, pattern):
    output = ''
    length = int(pattern[0:3], 2)
    input = pattern[3:]

    while input:
        key = input[0:length]
        # print('key: %s' % key)
        if not check_segment_end(length, key):
            # print(get_character(key), length, key)
            output += header[get_character(key)]
            input = input[length:]
        else:
            input = input[length:]
            length = int(input[0:3], 2)
            if length == 0:
                break
            input = input[3:]
    return output