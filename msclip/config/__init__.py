from .default import _C as config
from .default import update_config
from .default import save_config
from .default import export_deepspeed_config
from .models import MODEL_SPECS

__import__('pkg_resources').declare_namespace(__name__)
