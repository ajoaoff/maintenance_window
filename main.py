"""Main module of kytos/maintenance_window Kytos Network Application.

This NApp creates maintenance windows, allowing the maintenance of network devices (a switch, a board, a link) without receiving alerts. The circuits u
"""

from kytos.core import KytosNApp, log

from napps.kytos.maintenance_window import settings


class Main(KytosNApp):
    """Main class of kytos/maintenance_window NApp.

    This class is the entry point for this napp.
    """

    def setup(self):
        """Replace the '__init__' method for the KytosNApp subclass.

        The setup method is automatically called by the controller when your
        application is loaded.

        So, if you have any setup routine, insert it here.
        """
        pass

    def execute(self):
        """Run after the setup method execution.

        You can also use this method in loop mode if you add to the above setup
        method a line like the following example:

            self.execute_as_loop(30)  # 30-second interval.
        """
        pass

    def shutdown(self):
        """Run when your napp is unloaded.

        If you have some cleanup procedure, insert it here.
        """
        pass
