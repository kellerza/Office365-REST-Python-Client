from office365.delta_collection import DeltaCollection
from office365.outlook.mail.itemBody import ItemBody
from office365.outlook.mail.messages.message import Message
from office365.outlook.mail.recipient import Recipient
from office365.runtime.client_value_collection import ClientValueCollection


class MessageCollection(DeltaCollection):

    def __init__(self, context, resource_path=None):
        super(MessageCollection, self).__init__(context, Message, resource_path)

    def add(self, subject, body, to_recipients=None, **kwargs):
        """
        Create a draft of a new message in either JSON or MIME format.

        :param str subject: The subject of the message.
        :param str or ItemBody body: The body of the message. It can be in HTML or text format
        :param list[str] to_recipients:
        :rtype: Message
        """
        if to_recipients is None:
            to_recipients = []
        return super(MessageCollection, self).add(
            body=body if isinstance(body, ItemBody) else ItemBody(body),
            subject=subject,
            toRecipients=ClientValueCollection(Recipient, [Recipient.from_email(v) for v in to_recipients]),
            **kwargs)
