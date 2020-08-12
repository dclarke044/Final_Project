def create_classes(db):
    class moviedata(db.Model):
        __tablename__ = 'moviedata'

        index = db.Column(db.Integer, primary_key=True)
        imdb_title_id = db.Column(db.String(64))
        title = db.Column(db.String(64))
        year = db.Column(db.Integer)
        genre = db.Column(db.String(64))
        duration = db.Column(db.Integer)
        country = db.Column(db.String(64))
        director = db.Column(db.String(64))
        production_company = db.Column(db.String(64))
        budget = db.Column(db.Integer)
        total_votes = db.Column(db.Integer)
        median_vote = db.Column(db.Float)
        all18to29 = db.Column(db.Float)
        all30to44 = db.Column(db.Float)
        allover45 = db.Column(db.Float)
        males = db.Column(db.Float)
        males18to29 = db.Column(db.Float)
        males30to44 = db.Column(db.Float)
        malesover45 = db.Column(db.Float)
        females = db.Column(db.Float)
        females18to29 = db.Column(db.Float)
        females30to44 = db.Column(db.Float)
        femalesover45 = db.Column(db.Float)
        rating_class = db.Column(db.String(64))

        def __repr__(self):
            return '<moviedata %r>' % (self.name)
            
    return moviedata