from __future__ import absolute_import

import six

from rest_framework.response import Response

from sentry.api.base import Endpoint
from sentry.api.bases.group import GroupPermission
from sentry.api.exceptions import ResourceDoesNotExist
from sentry.api.serializers import DetailedEventSerializer, serialize
from sentry.models import Event


class EventDetailsEndpoint(Endpoint):
    permission_classes = (GroupPermission, )

    def get(self, request, event_id):
        """
        Retrieve an Event
        `````````````````

        This endpoint returns the data for a specific event.  The event ID
        is the event as it appears in the Sentry database and not the event
        ID that is reported by the client upon submission.
        """
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            raise ResourceDoesNotExist

        self.check_object_permissions(request, event.group)

        Event.objects.bind_nodes([event], 'data')

        data = serialize(event, request.user, DetailedEventSerializer())

        next_event = event.next_event
        prev_event = event.prev_event
        data['nextEventID'] = next_event and six.text_type(next_event.id)
        data['previousEventID'] = prev_event and six.text_type(prev_event.id)

        return Response(data)
