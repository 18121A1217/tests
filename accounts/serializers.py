from rest_framework import serializers
from accounts.models import User, UserCart, UserProfile, UserCartProduct, UserLoginOtp


class UserModelSerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    date_of_birth = serializers.SerializerMethodField()
    image = serializers.ImageField(source='models.UserProfile', max_length=254, use_url=True, allow_null=True)

    def get_gender(self, obj):
        return obj.owner.gender

    def get_name(selfself, obj):
        return obj.owner.name

    def get_date_of_birth(self, obj):
        return obj.owner.date_of_birth

    class Meta:
        model = User
        fields = (
            'phone_number',
            'name',
            'date_of_birth',
            'gender',
            'image',
        )


class UserCartModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCart
        fields = '__all__'
