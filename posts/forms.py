# posts/forms.py
from django import forms
from .models import Post, Author


class PostForm(forms.ModelForm):
    author_name = forms.CharField(label="Author Name")

    """
    Form for creating and updating Post objects.
    Fields:
    - title: CharField for the post title.
    - content: TextField for the post content.
    - author_name: Custom CharField (not stored in Post model directly).
    """

    class Meta:
        model = Post
        fields = ["title", "content", "author_name"]

    def __init__(self, *args, **kwargs):
        instance = kwargs.get("instance")
        super().__init__(*args, **kwargs)

        if instance and instance.author:
            # Pre-fill the author's name when editing
            self.fields["author_name"].initial = instance.author.name
            # Make author_name read-only when editing an existing post
            self.fields["author_name"].disabled = True

    def save(self, commit=True):
        """
        Custom save method:
        - Creates or retrieves the Author object.
        - Ensures Post.author is always assigned before saving.
        """
        author_name = self.cleaned_data.get("author_name")

        # Reuse the author if editing and the field is disabled
        if self.instance and self.instance.pk and self.fields["author_name"].disabled:
            author = self.instance.author
        else:
            # Create or fetch the author
            author, _ = Author.objects.get_or_create(name=author_name)

        # Build the Post object but don’t commit yet
        post = super().save(commit=False)
        post.author = author

        if commit:
            post.save()

        return post
