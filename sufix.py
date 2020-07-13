#!/usr/bin/env python3

import os
import re
import sys
import click


not_changed_enything = "فایل وارد شده زیرنویس نیست، دقت کنید که فایل با پسوند .srt نیاز است!"
working_dir = os.getcwd()
subtitles_path = ""  # example: "/home/sina/subtitles" or leave it empty


class SubtitleFix:
    def __init__(self):
        self.time = '\d\d:\d\d:\d\d,\d\d\d'
        self.number = u'۰۱۲۳۴۵۶۷۸۹'

        self.string = ''

    def fix_encoding(self):
        # assert isinstance(self.string, str), repr(self.string)

        try:
            # self.string.decode(encoding='utf-8', errors='strict')
            self.string = self.string.decode('utf-8')
            return 'utf-8'
        except (UnicodeError, UnicodeDecodeError):
            pass

        try:
            # self.string.decode(encoding='utf-16', errors='strict')
            self.string = self.string.decode('utf-16')
            return 'utf-16'
        except (UnicodeError, UnicodeDecodeError):
            pass

        self.string = self.string.decode(encoding='windows-1256', errors='strict')
        return 'windows-1256'

    def fix_italic(self):
        self.string = self.string.replace('<i>', '')
        self.string = self.string.replace('</i>', '')

    def fix_arabic(self):
        self.string = self.string.replace(u'ي', u'ی')
        self.string = self.string.replace(u'ك', u'ک')

    def fix_question_mark(self):
        # quistion mark in persina is ؟ not ?
        self.string = self.string.replace('?', u'؟')

    def fix_other(self):
        self.string = self.string.replace(u'\u202B', u'')

        lines = self.string.split('\n')
        string = ''

        for line in lines:
            if re.match('^%s\s-->\s%s$' % (self.time, self.time), line):
                string += line
            elif re.match('^%s\s-->\s%s$' % (self.time, self.time), line[:-1]):
                string += line
            elif line.strip() == '':
                string += line
            elif re.match('^\d+$', line):
                string += line
            elif re.match('^\d+$', line[:-1]):
                string += line
            else:
                # this should be subtitle
                s = re.match('^([\.!?]*)', line)

                try:
                    line = re.sub('^%s' % s.group(), '', line)
                except:
                    pass

                # use persian numbers
                for i in range(0, 10):
                    line = line.replace(str(i), self.number[i])

                # for ltr problems some peoples put '-' on EOL
                # it should be in start
                if len(line) != 0 and line[-1] == '-':
                    line = '- %s' % line[:-1]
                line += s.group()

                # put rtl char in start of line (it forces some player to show that line rtl
                string += u'\u202B' + line  # str(line, 'utf-8')

            # noting to see here
            string += '\n'

            self.string = string

    def decode_string(self, string):
        self.string = string
        print(f"Fixing Encoding...  ", end="")
        print(f"\r\t\t\t\t\t", end="")
        enc = self.fix_encoding()
        click.secho(f"subtitle encoding fixed: {enc}", fg="green")

        print(f"Fixing Italic...  ", end="")
        print(f"\r\t\t\t\t\t", end="")
        self.fix_italic()
        click.secho(f"subtitle italic fixed", fg="green")

        print(f"Fixing Arabic chars...  ", end="")
        print(f"\r\t\t\t\t\t", end="")
        self.fix_arabic()
        click.secho(f"subtitle Arabic chars fixed", fg="green")

        print(f"Fixing question marks...  ", end="")
        print(f"\r\t\t\t\t\t", end="")
        self.fix_question_mark()
        click.secho(f"subtitle question marks fixed", fg="green")

        print(f"Fixing other problems...  ", end="")
        print(f"\r\t\t\t\t\t", end="")
        self.fix_other()
        click.secho(f"subtitle other problems fixed", fg="green")

        return self.string


def sufix(path):
    subfixer = SubtitleFix()

    if path[-4:] != '.srt':
        click.secho(not_changed_enything, fg="red")
        sys.exit(0)
    else:
        with open(path, 'rb') as f:
            lines = f.read((2**10)**2)
            f.close()
            lines = subfixer.decode_string(lines)
            ctr = 0
            click.secho()
            for line in lines.split("\n"):
                if ctr >= 30:
                    break
                print(line)
                ctr += 1

            if click.confirm(click.style("These are the first lines as demo, enter yes to confirm changes", fg="bright_blue")):
                bacup_path = path.replace(".srt", "-backup.srt")
                os.rename(path, bacup_path)
                click.secho(f"Warning: The original file witll be renamed to {bacup_path} as backup!", fg="yellow")
                with open(path, 'w') as fnew:
                    fnew.write(str(lines))
                    fnew.close()
                    click.secho(f"File saved to {path}", fg="green")
            else:
                click.secho("Aborted!, exiting...", fg="bright_red")
                sys.exit(0)


class CliGroup(click.Group):
    def list_commands(self, ctx):
        return [
            "fix"
            "help"
        ]


@click.group(cls=CliGroup)
def cli():
    pass


@cli.command()
@click.option('-fp', '--fullpath', default=None)
@click.option('-i', '--input', default=None)
@click.option('-p', '--path', default=lambda: os.getcwd())
@click.option('-cs', '--custompath', default=subtitles_path)
def fix(fullpath, input, path, custom_path):
    if fullpath is not None:
        file_path = fullpath

    if input is None:
        click.echo("Not a valid filepath")
        sys.exit(0)
    else:
        if custom_path != "":
            path = custom_path
        file_path = path + "/" + input

    sufix(file_path)


if __name__ == '__main__':
    cli()
