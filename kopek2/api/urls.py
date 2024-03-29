from rest_framework.routers import DefaultRouter
from kopek2.api.views import *
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

router.register('color', ColorViewSet)
router.register('size', SizeViewSet)
router.register('country', CountryViewSet)
router.register('city', CityViewSet)
router.register('branch', BranchViewSet)
router.register('hospital', HospitalViewSet)
router.register('illness', IllnessViewSet)
router.register('illnesstype', IllnessTypeViewSet)
router.register('doctor', DoctorViewSet)
router.register('gadgettype', GadgetTypeViewSet)
router.register('award', AwardViewSet)
router.register('judge', JudgeViewSet)
router.register('owner', OwnerViewSet)
router.register('challenge', ChallengeViewSet)
router.register('pet', PetViewSet)
router.register('race', RaceViewSet)
router.register('petchallenge', PetChallengeViewSet)
router.register('petillness', PetIllnessViewSet)

urlpatterns = router.urls

