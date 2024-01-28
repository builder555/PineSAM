import subprocess


def run_command(command: str) -> tuple[bool, str]:
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return True, result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return False, e.stderr.strip()


class ServiceCheck:
    def __init__(self, name: str, command: str, recommend: str = ""):
        self.command = command
        self.name = name
        self.recommend = recommend
        self.success = False

    def run(self) -> bool:
        self.success, _ = run_command(self.command)
        return self.success


def run_checks() -> tuple[bool, list[str]]:
    checks = [
        ServiceCheck("BlueZ", "bluetoothd -v", recommend="Install BlueZ"),
        ServiceCheck(
            "bluetooth.service active",
            "systemctl status bluetooth.service",
            recommend="Install/Start bluetooth.service",
        ),
        ServiceCheck(
            "D-Bus configuration file for Bluetooth",
            "test -f /etc/dbus-1/system.d/bluetooth.conf || test -f /usr/share/dbus-1/system.d/bluetooth.conf || test -f /var/lib/dbus-1/system.d/bluetooth.conf",
            recommend="Install D-Bus configuration file for Bluetooth",
        ),
    ]
    all_passed = all([c.run() for c in checks])
    return all_passed, [
        f"{c.name} check failed. {c.recommend}" for c in checks if not c.success
    ]


def main():
    all_passed, errors = run_checks()
    if not all_passed:
        print("Bluetooth check failed:")
        print("\n".join(errors))
        return
    success, output = run_command("journalctl -u bluetooth.service -n 10")
    if success:
        print("Last 10 lines of bluetooth.service logs:\n" + output)
    else:
        print("Failed to retrieve bluetooth.service logs.")


if __name__ == "__main__":
    main()
