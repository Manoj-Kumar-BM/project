class Exhibit:
    def __init__(self, exhibit_id, title, description, date):
        self.exhibit_id = exhibit_id
        self.title = title
        self.description = description
        self.date = date

    def __str__(self):
        return f"Exhibit ID: {self.exhibit_id}, Title: {self.title}, Date: {self.date}, Description: {self.description}"


class Artist:
    def __init__(self, artist_id, name):
        self.artist_id = artist_id
        self.name = name

    def __str__(self):
        return f"Artist ID: {self.artist_id}, Name: {self.name}"


class Submission:
    def __init__(self, submission_id, exhibit_id, artist_id, artwork_title):
        self.submission_id = submission_id
        self.exhibit_id = exhibit_id
        self.artist_id = artist_id
        self.artwork_title = artwork_title

    def __str__(self):
        return f"Submission ID: {self.submission_id}, Exhibit ID: {self.exhibit_id}, Artist ID: {self.artist_id}, Artwork Title: {self.artwork_title}"


class ExhibitManager:
    def __init__(self):
        self.exhibits = {}
        self.artists = {}
        self.submissions = {}

    def create_exhibit(self, exhibit_id, title, description, date):
        exhibit = Exhibit(exhibit_id, title, description, date)
        self.exhibits[exhibit_id] = exhibit

    def read_exhibit(self, exhibit_id):
        return self.exhibits.get(exhibit_id)

    def update_exhibit(self, exhibit_id, title=None, description=None, date=None):
        exhibit = self.exhibits.get(exhibit_id)
        if exhibit:
            if title:
                exhibit.title = title
            if description:
                exhibit.description = description
            if date:
                exhibit.date = date

    def delete_exhibit(self, exhibit_id):
        if exhibit_id in self.exhibits:
            del self.exhibits[exhibit_id]

    def coordinate_art_exhibits(self, exhibit_id):
        exhibit = self.read_exhibit(exhibit_id)
        if exhibit:
            
            print(f"Coordinating exhibit: {exhibit}")

    def manage_artist_submissions(self, submission_id, exhibit_id, artist_id, artwork_title):
        submission = Submission(submission_id, exhibit_id, artist_id, artwork_title)
        self.submissions[submission_id] = submission

    def get_submission(self, submission_id):
        return self.submissions.get(submission_id)


if __name__ == "__main__":
    manager = ExhibitManager()

    
    manager.create_exhibit(1, "clay modeling", "making something out of clay", "2024-08-20")
    manager.create_exhibit(2, "Dance", "from that involves movement of body", "2024-08-21")

    
    print(manager.read_exhibit(1))

    
    manager.update_exhibit(1, date="2024-05-16")

    
    manager.delete_exhibit(2)

   
    manager.coordinate_art_exhibits(1)

    
    manager.manage_artist_submissions(101, 1, "A123", "making something out of clay")
    print(manager.get_submission(101))
