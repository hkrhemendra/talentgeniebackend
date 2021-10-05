from passion_pro.models.competition import Competitions
from flask_marshmallow import Marshmallow
from marshmallow import fields

from passion_pro.models import categories, competition

from passion_pro.models import batches

ma = Marshmallow()

from ..models.users import Users
from ..models.categories import Categories
from ..models.batches import Batches
from ..models.courses import Courses
from ..models.batches_courses import batches_courses
from ..models.users_batches import users_batches
from ..models.users_categories import users_categories


class CoursesSchema(ma.SQLAlchemyAutoSchema):
    #batches = ma.Nested(BatchesSchema,many=True)
    class Meta:
        # model = Courses
        fields = ('id', 'course_name', 'course_code' , 'discription' , 'minage' , 'maxage' , 'coursetype' , 'rating', 'level', 'broucher' , 'thumbnail_image' , 'video' ,'course_code','prerequisites')


class BatchesSchema(ma.SQLAlchemyAutoSchema):
    courses = ma.Nested(CoursesSchema,many=True)
    class Meta:
        # model = Batches
        fields = ('id', 'batch_size' , 'price' , 'batch_start' , 'batch_end' , 'time_from' , 'time_to' , 'rating','weekDays' , 'is_active' , 'remark' ,'discription','discount' , 'courses')
        ordered = True
        
class CategoriesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ('id','name' ,'discription', 'ranking' , 'image', 'video')



class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        # model = Users
        fields = ('id', 'firstname','lastname', 'email','profile_picture','experience' , 'qualifications' , 'doc1' , 'doc2' , 'doc3' , 'doc4')
        

class CompetitionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ('id', 'title', 'competition_start_time', 'competition_end_time', 'registration_start', 'registration_end', 'category_fk', 'minage', 'maxage', 'gender', 'remark', 'discription','rating','requirements', 'image')


class UserBatchesSchema(ma.SQLAlchemyAutoSchema):
    batches = ma.Nested(BatchesSchema, many=True)
    class Meta:
        # model = Users
        fields = ('id', 'batches','firstname','lastname', 'email','dob','profile_picture','is_teacher','is_admin' , 'phone1' , 'phone2' , 'address' , 'experience' , 'qualifications' , 'doc1' , 'doc2' , 'doc3' , 'doc4' , 'remark' , 'confirmed_at' , 'updated_at')

class UsersCategoriesSchema(ma.SQLAlchemyAutoSchema):
    categories = ma.Nested(CategoriesSchema, many=True)
    class Meta:
        fields = ('id','firstname','lastname', 'email','dob','profile_picture','is_teacher','is_admin' , 'phone1' , 'phone2' , 'address' , 'experience' , 'qualifications' , 'doc1' , 'doc2' , 'doc3' , 'doc4' , 'remark' , 'confirmed_at' , 'updated_at' ,'categories')

class PreviousWinnersSchema(ma.SQLAlchemyAutoSchema):
    comp = ma.Nested(CompetitionSchema, many= True)
    user = ma.Nested(UserSchema)
    class Meta:
        fields = ('user_fk', 'competition_fk', 'comp', 'user')
# load_instance = True

