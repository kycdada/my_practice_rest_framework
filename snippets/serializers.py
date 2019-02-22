from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

#'''by serializer'''
#class SnippetSerializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only=True)
#    title = serializers.CharField(require=False, allow_blank=True, max_length=100)
#    code = serializers.CharField(style={'base_template': 'textarea.html'})
#    linenos = serializers.BooleanField(required=False)
#    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default="friendly")
#    
#    def create(self,validated_data):
#        
#        # create and return a new "Snippet" instance, given the validated data.
#        return Snippet.Objects.create(**validated_data)
#        
#    def update(self, instance, validated_data):
#        # update and return an existing 'Snippet' instance, given the validated data.
#        
#        instance.title = validated_data.get('title' instance.title)
#        inatance.code = validated_data.get('code', instance.code)
#        instance.linenos = validated_data.get('linenos', instance.linenos)
#        instance.language = validated_data.get('language', instance.language)
#        instance style = validated_data.get('style', instance.style)
#        instance.save()
#        return insatance

'''by ModelSerializer'''
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight',format='html')
    
    class Meta:
        model = Snippet
        fields = ('url','id','title','highlight','owner','code','linenos','language','style')
        
#        id = IntegerField(label='ID', read_only=True)
#        title = CharField(allow_blank=True, max_length=100, required=False)
#        code = CharField(style={'base_template': 'textarea.html'})
#        linenos = BooleanField(required=False)
#        language = ChoiceField(choices=[('Clipper', 'FoxPro'), ('Cucumber', 'Gherkin'), ('RobotFramework', 'RobotFramework'), ('abap', 'ABAP'), ('ada', 'Ada')...
#        style = ChoiceField(choices=[('autumn', 'autumn'), ('borland', 'borland'), ('bw', 'bw'), ('colorful', 'colorful')...


'''make for userlist'''
class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True,view_name='snippet-detail', read_only=True)
    
    class Meta:
        model =User
        fields=('url','id', 'username', 'snippets')
    
