import json
import pdb

from django.shortcuts import render_to_response
from django.template import RequestContext

from apps.cserver_comm.cserver_communicator import get_full_graph_json_str, get_concept_data
from apps.user_management.models import Profile


def get_agfk_app(request):
    if request.user.is_authenticated():
        uprof, created = Profile.objects.get_or_create(pk=request.user.pk)
        lset = set()
        sset = set()
        [lset.add(lc.id) for lc in uprof.learned.all()]
        [sset.add(sc.id) for sc in uprof.starred.all()]
        concepts = {"concepts": [{"id": uid, "learned": uid in lset, "starred": uid in sset} for uid in lset.union(sset)]}
    else:
        concepts = {"concepts": []}

    concept_tag = request.path.split("/")[-1].split("#")[0]
    concept_data = get_concept_data(concept_tag)
    # pdb.set_trace()
    return render_to_response("agfk-app.html",
                              {"full_graph_skeleton": get_full_graph_json_str(), "user_data": json.dumps(concepts), "concept_data": concept_data},
                              context_instance=RequestContext(request))

