from terra_classic_sdk.client.lcd import LCDClient

terra = LCDClient(chain_id="columbus-5", url="https://terra-classic-lcd.publicnode.com")


def test_validators_with_voting_power():
    validators_with_voting_power = terra.utils.validators_with_voting_power()
    print(validators_with_voting_power)
    assert validators_with_voting_power is not None
