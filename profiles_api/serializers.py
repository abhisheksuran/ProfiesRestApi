from rest_framework import serializers


# def user_validator(nm):
#     """Custom validator for name serializer"""
#     if 'k' in nm or 'K' in nm:
#         raise serializers.ValidationError("Name should not contain 'K'")
#     return nm

class HelloSerializer(serializers.Serializer):
    """Serializea a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)
    # name = serializers.CharField(validators=[user_validator])
