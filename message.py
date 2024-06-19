from twilio.rest import Client


client =  Client('','')

def send_message(number):
    # msg = f"Have you heard of TEMPX? It’s been a game-changer for Candidates
    #   searching for Jobs. You can download app from tempx.ca to explore more.
    #     Let us know if you need help getting started. Email:admin@tempx.ca"
    # "Invited by friend!"

    msg="""Your friend name referred you for next generation employment app TEMPX(tempx.ca).Please download from 
    Apple store:
    https://apps.apple.com/in/app/tempx/id6461161140\n
    Playstore:
    https://play.google.com/store/apps/details?id=com.tempx.tempx_project\n
    Referral-Bonus Programme:
    Compensation for every reference that sign in they will be paid 1 dollar per reference,once 10 references have signed in they will be paid a signup bonus of $100,once 50 references signup they will get a additional bonus of $500,and once they signup 100 people they will be rewarded with $1000.
    """
    message = client.messages.create(
        body = msg,
        from_='+',
        to=f'+1{number}'
    )

    print(message.body)


