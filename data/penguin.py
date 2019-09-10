
from gino import Gino
db = Gino()


class Penguin(db.Model):
    __tablename__ = 'penguin'

    id = db.Column(db.Integer, primary_key=True, server_default=db.text("nextval('\"penguin_id_seq\"'::regclass)"))
    username = db.Column(db.String(12), nullable=False, unique=True)
    nickname = db.Column(db.String(30), nullable=False)
    password = db.Column(db.CHAR(60), nullable=False)
    email = db.Column(db.String(255), nullable=False, index=True)
    registration_date = db.Column(db.DateTime, nullable=False, server_default=db.text("now()"))
    active = db.Column(db.Boolean, nullable=False, server_default=db.text("false"))
    safe_chat = db.Column(db.Boolean, nullable=False, server_default=db.text("false"))
    last_paycheck = db.Column(db.DateTime, nullable=False, server_default=db.text("now()"))
    minutes_played = db.Column(db.Integer, nullable=False, server_default=db.text("0"))
    moderator = db.Column(db.Boolean, nullable=False, server_default=db.text("false"))
    stealth_moderator = db.Column(db.Boolean, nullable=False, server_default=db.text("false"))
    character = db.Column(db.ForeignKey('character.id', ondelete='CASCADE', onupdate='CASCADE'))
    igloo = db.Column(db.ForeignKey('penguin_igloo_room.id', ondelete='CASCADE', onupdate='CASCADE'))
    coins = db.Column(db.Integer, nullable=False, server_default=db.text("500"))
    color = db.Column(db.ForeignKey('item.id', ondelete='CASCADE', onupdate='CASCADE'))
    head = db.Column(db.ForeignKey('item.id', ondelete='CASCADE', onupdate='CASCADE'))
    face = db.Column(db.ForeignKey('item.id', ondelete='CASCADE', onupdate='CASCADE'))
    neck = db.Column(db.ForeignKey('item.id', ondelete='CASCADE', onupdate='CASCADE'))
    body = db.Column(db.ForeignKey('item.id', ondelete='CASCADE', onupdate='CASCADE'))
    hand = db.Column(db.ForeignKey('item.id', ondelete='CASCADE', onupdate='CASCADE'))
    feet = db.Column(db.ForeignKey('item.id', ondelete='CASCADE', onupdate='CASCADE'))
    photo = db.Column(db.ForeignKey('item.id', ondelete='CASCADE', onupdate='CASCADE'))
    flag = db.Column(db.ForeignKey('item.id', ondelete='CASCADE', onupdate='CASCADE'))
    permaban = db.Column(db.Boolean, nullable=False, server_default=db.text("false"))
    book_modified = db.Column(db.SmallInteger, nullable=False, server_default=db.text("0"))
    book_color = db.Column(db.SmallInteger, nullable=False, server_default=db.text("1"))
    book_highlight = db.Column(db.SmallInteger, nullable=False, server_default=db.text("1"))
    book_pattern = db.Column(db.SmallInteger, nullable=False, server_default=db.text("0"))
    book_icon = db.Column(db.SmallInteger, nullable=False, server_default=db.text("1"))
    agent_status = db.Column(db.Boolean, nullable=False, server_default=db.text("false"))
    field_op_status = db.Column(db.SmallInteger, nullable=False, server_default=db.text("0"))
    career_medals = db.Column(db.Integer, nullable=False, server_default=db.text("0"))
    agent_medals = db.Column(db.Integer, nullable=False, server_default=db.text("0"))
    last_field_op = db.Column(db.DateTime, nullable=False, server_default=db.text("now()"))
    ninja_rank = db.Column(db.SmallInteger, nullable=False, server_default=db.text("0"))
    ninja_progress = db.Column(db.SmallInteger, nullable=False, server_default=db.text("0"))
    fire_ninja_rank = db.Column(db.SmallInteger, nullable=False, server_default=db.text("0"))
    fire_ninja_progress = db.Column(db.SmallInteger, nullable=False, server_default=db.text("0"))
    water_ninja_rank = db.Column(db.SmallInteger, nullable=False, server_default=db.text("0"))
    water_ninja_progress = db.Column(db.SmallInteger, nullable=False, server_default=db.text("0"))
    ninja_matches_won = db.Column(db.Integer, nullable=False, server_default=db.text("0"))
    fire_matches_won = db.Column(db.Integer, nullable=False, server_default=db.text("0"))
    water_matches_won = db.Column(db.Integer, nullable=False, server_default=db.text("0"))
    rainbow_adoptability = db.Column(db.SmallInteger, nullable=False, server_default=db.text("0"))
    has_dug = db.Column(db.Boolean, nullable=False, server_default=db.text("false"))
    nuggets = db.Column(db.SmallInteger, nullable=False, server_default=db.text("0"))
    opened_playercard = db.Column(db.Boolean, nullable=False, server_default=db.text("false"))
    special_wave = db.Column(db.Boolean, nullable=False, server_default=db.text("false"))
    special_dance = db.Column(db.Boolean, nullable=False, server_default=db.text("false"))
    special_snowball = db.Column(db.Boolean, nullable=False, server_default=db.text("false"))
    map_category = db.Column(db.SmallInteger, nullable=False, server_default=db.text("0"))
    status_field = db.Column(db.Integer, nullable=False, server_default=db.text("0"))
    timer_active = db.Column(db.Boolean, nullable=False, server_default=db.text("false"))
    timer_start = db.Column(db.Time, nullable=False, server_default=db.text("'00:00:00'::time without time zone"))
    timer_end = db.Column(db.Time, nullable=False, server_default=db.text("'23:59:59'::time without time zone"))
    approval_en = db.Column(db.Boolean, nullable=False, server_default=db.text("false"))
    approval_pt = db.Column(db.Boolean, nullable=False, server_default=db.text("false"))
    approval_fr = db.Column(db.Boolean, nullable=False, server_default=db.text("false"))
    approval_es = db.Column(db.Boolean, nullable=False, server_default=db.text("false"))
    approval_de = db.Column(db.Boolean, nullable=False, server_default=db.text("false"))
    approval_ru = db.Column(db.Boolean, nullable=False, server_default=db.text("false"))
    rejection_en = db.Column(db.Boolean, nullable=False, server_default=db.text("false"))
    rejection_pt = db.Column(db.Boolean, nullable=False, server_default=db.text("false"))
    rejection_fr = db.Column(db.Boolean, nullable=False, server_default=db.text("false"))
    rejection_es = db.Column(db.Boolean, nullable=False, server_default=db.text("false"))
    rejection_de = db.Column(db.Boolean, nullable=False, server_default=db.text("false"))
    rejection_ru = db.Column(db.Boolean, nullable=False, server_default=db.text("false"))

class PenguinPostcard(db.Model):
    __tablename__ = 'penguin_postcard'

    id = db.Column(db.Integer, primary_key=True,
                   server_default=db.text("nextval('\"penguin_postcard_id_seq\"'::regclass)"))
    penguin_id = db.Column(db.ForeignKey('penguin.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False,
                           index=True)
    sender_id = db.Column(db.ForeignKey('penguin.id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    postcard_id = db.Column(db.ForeignKey('postcard.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    send_date = db.Column(db.DateTime, nullable=False, server_default=db.text("now()"))
    details = db.Column(db.String(255), nullable=False, server_default=db.text("''::character varying"))
    has_read = db.Column(db.Boolean, nullable=False, server_default=db.text("false"))


class PenguinItem(db.Model):
    __tablename__ = 'penguin_item'

    penguin_id = db.Column(db.ForeignKey('penguin.id', ondelete='CASCADE', onupdate='CASCADE'),
                           primary_key=True, nullable=False)
    item_id = db.Column(db.ForeignKey('item.id', ondelete='CASCADE', onupdate='CASCADE'),
                        primary_key=True, nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
