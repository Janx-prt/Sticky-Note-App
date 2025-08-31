from django.db import models


class Author(models.Model):
    """
    Model representing the author of a sticky note.
    Fields:
    - name: CharField for the author's name.
    """
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        # String representation of the author (shows the name)
        return self.name


class Post(models.Model):
    """
    Model representing a sticky note post.
    Fields:
    - title: CharField for the post title (max length 255).
    - content: TextField for the note content.
    - created_at: DateTimeField auto-set when created.
    Relationships:
    - author: ForeignKey to Author (required).
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        null=False,   # author is required
        blank=False
    )

    def __str__(self):
        # Always display title + author safely
        return f"{self.title} by {self.author.name if self.author_id else 'Unknown'}"
