import platform
from lele.Metaprogramming import try_import

def get_device_specs():
    specs = {
        "system": platform.system(),
        "platform": platform.platform(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
    }
    
    if torch := try_import("torch"):
        specs["pytorch_version"] = torch.__version__
        if torch.cuda.is_available():
            specs["device_type"] = "cuda"
            specs["device_count"] = torch.cuda.device_count()
            # Get details for the current/first GPU
            props = torch.cuda.get_device_properties(0) 
            specs["gpu_name"] = props.name
            # Convert bytes to GB for readability
            specs["gpu_total_memory_gb"] = round(props.total_memory / (1024**3), 2)
            specs["cuda_version"] = torch.version.cuda
        elif torch.backends.mps.is_available():
            specs["device_type"] = "mps" # Apple Silicon
        else:
            specs["device_type"] = "cpu"
            
    return specs

def test_():
    print(get_device_specs())
