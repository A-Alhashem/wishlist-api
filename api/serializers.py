from rest_framework import serializers
from items.models import Item, FavoriteItem
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['first_name', 'last_name',]


class UserFavSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	class Meta:
		model = FavoriteItem
		fields = ['user',]




class ItemListSerializer(serializers.ModelSerializer):

	fav_count = serializers.SerializerMethodField()

	details = serializers.HyperlinkedIdentityField(
		view_name = 'api-detail',
		lookup_field = 'id',
		lookup_url_kwarg = 'api_id'
		)

	added_by = UserSerializer()

	class Meta:
		model = Item
		fields = ['image', 'name', 'description', 'added_by', 'details', 'fav_count',]

	def get_fav_count(self, obj):
		fav = FavoriteItem.objects.filter(item=obj)
		return fav.count()
		# return (obj.favoriteitem_set.all().count())


class ItemDetailSerializer(serializers.ModelSerializer):

	fav_by = serializers.SerializerMethodField()

	class Meta:
		model = Item
		fields = ['image', 'name', 'description', 'fav_by',]

	def get_fav_by(self, obj):
		favs = FavoriteItem.objects.filter(item=obj)
		return UserFavSerializer(favs, many=True).data

		# favs = obj.favoriteitem_set.all()

