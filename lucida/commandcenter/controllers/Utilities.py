from werkzeug import secure_filename


# Checks if the extension of the input file is valid.
def check_image_extension(upload_file):
	if upload_file is None:
		return
	filename = secure_filename(upload_file.filename)
	if not filename:
		return
	valid_extensions = ['png', 'PNG', 'jpg', 'JPG', 'bmp', 'BMP', \
		'gif', 'GIF']
	allowed_extensions = set(valid_extensions)
	if not (('.' in filename) and \
		(filename.rsplit('.', 1)[1] in allowed_extensions)):
		raise RuntimeError('Invalid file: extension must be one of ' \
			+ str(valid_extensions))

# Checks if the text input is valid.
def check_text_input(text_input):
	if text_input is None:
		return
	if len(text_input) >= 200:
		raise RuntimeError('Please input less than 200 characters')
	if text_input.isspace():
		raise RuntimeError('Empty text is not allowed')