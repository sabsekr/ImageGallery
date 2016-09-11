from django import forms

"""
Form for uploading images. Contains a field to upload an image and a text field to enter the hashtag
"""
class ImageUploadForm(forms.Form):
    image_upload = forms.FileField(
        label='Select an image',
    )
    tag_text = forms.CharField(
        max_length=128,
        help_text="Please enter your hash tag"
    )

