import sublime, sublime_plugin, time

class MakeSumCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        result = 0;
        regions = self.view.sel();

        try:
            for i in range(0, len(regions)):
                region  = regions[i];
                text    = self.view.substr(region);
                result += float(text);

                if(i >= len(regions) -1):
                    self.view.replace(
                        edit,
                        region,
                        text + "\n Result: " + str(result)
                    );
        except:
            pass;


