def loadEnv(default=".env"):
    # Load environment variables as a dictionary
    env = {}
    with open(f"{default}", "r") as f:
        for line in f:
            if line[0] != '#':
                key, value = line.strip().split('=')
                env[key] = value
    return env