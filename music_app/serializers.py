from rest_framework import serializers

from music_app.models import Music, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # print(representation)
        category = CategorySerializer(Category.objects.get(music=instance.id)).data # чтобы получить категорию определенную из баз данных по id
        print(category)
        print(representation)
        representation['category'] = category # вместо id выйдет его значение

        return representation



