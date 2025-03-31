from apps.advertisements.serializers import AdvertisementSerializer


class AdvertUpdateSerializer(AdvertisementSerializer):
    # Only for schema generation, not actually used.
    # because DRF-YASG does not support partial.
    def get_fields(self):
        new_fields = {}
        for name, field in super().get_fields().items():
            field.required = False
            new_fields[name] = field
        return new_fields
