import shutil


def check_tool(tool_name):

    return shutil.which(tool_name) is not None


def validate_prerequisites():

    return {
        "python": check_tool("python"),
        "git": check_tool("git"),
        "docker": check_tool("docker"),
        "kubectl": check_tool("kubectl")
    }