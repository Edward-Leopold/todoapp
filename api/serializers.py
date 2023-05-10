from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    # Вы можете добавить дополнительные поля в ModelSerializer
    created = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()
    
    class Meta:
        model = Todo
        fields = ['id','title','memo','created','completed']

class TodoToggleCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id'] # why need to show id?
        # Вы можете указать несколько полей как доступные только для чтения. 
        read_only_fields = ['title','memo','created','completed']

# Класс ModelSerializer предоставляет ярлык, позволяющий автоматически создать класс Serializer с полями, соответствующими полям модели.
# Если вы хотите, чтобы в сериализаторе модели использовалось только подмножество полей по умолчанию,
# вы можете сделать это с помощью опций fields или exclude, как и в случае с ModelForm.
# Настоятельно рекомендуется явно задавать все поля, которые должны быть сериализованы,
# с помощью атрибута fields. Это уменьшит вероятность непреднамеренного раскрытия данных при изменении ваших моделей.