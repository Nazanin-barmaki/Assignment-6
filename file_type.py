name=list(input('hey body enter your file name:) '))

split=name.index('.')

del name[:split+1]

file_type=''.join(name)

print(f'Your file type is: {file_type}')