import pytest
from imprezy.models import Party, Gift
from imprezy.views import AddParty


@pytest.mark.django_db
def test_add_party_to_base(entry):
    response = entry.post(f'add_party/', {'party_name': 'ślub', 'party_date': '08/02/2022',
                                           'party_time': '17:00', 'description': 'Ola i Marek'})
    assert response.status_code == 302
    assert Party.objects.count() == 1
    assert Party.objects.get(party_name="ślub")







