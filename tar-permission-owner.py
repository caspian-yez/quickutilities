#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
import sys
import os
import subprocess
import json


def run_cmd(cmd: list, current_working_dir: str = None, use_shell=False) -> dict:
    cmd_result = subprocess.run(
        cmd, capture_output=True, cwd=current_working_dir, shell=use_shell
    )
    json_result = {
        "cmd": cmd,
        "returncode": cmd_result.returncode,
        "stderr": cmd_result.stderr.decode(),
        "stdout": cmd_result.stdout.decode(),
    }
    if 0 != json_result["returncode"]:
        print(json.dumps(json_result, ensure_ascii=False, indent=4, sort_keys=True))
    return json_result


def main():
    workspace = "/tmp/tar-po-workspace"
    cmd_mkdir = ["mkdir", "-p", workspace]
    print("Begin processing: {}".format(sys.argv[1]))
    run_cmd(cmd_mkdir)

    cmd_clean_up = 'rm -rfv "{}/"*'.format(workspace)
    run_cmd(cmd=cmd_clean_up, use_shell=True)

    cmd_extract = ["tar", "-xf", sys.argv[1], "-C", workspace]
    run_cmd(cmd_extract)

    new_file = "new-{}".format(os.path.basename(sys.argv[1]))
    wd_current = os.getcwd()
    cmd_compress = 'tar --owner=root --group=root -cJf "{}" *'.format(new_file)
    run_cmd(cmd=cmd_compress, current_working_dir=workspace, use_shell=True)

    new_file_path = os.path.join(workspace, new_file)
    atime = os.path.getatime(sys.argv[1])
    mtime = os.path.getmtime(sys.argv[1])
    cmd_compare = ["pkgdiff", sys.argv[1], new_file_path]
    compare_result = run_cmd(cmd_compare)
    if "UNCHANGED" in compare_result["stdout"]:
        cmd_copy_file = ["cp", new_file_path, sys.argv[1]]
        run_cmd(cmd_copy_file)
        os.utime(sys.argv[1], (atime, mtime))
    else:
        print("Error happend in while processing {}".format(sys.argv[1]))
        os.utime(new_file_path, (atime, mtime))
        cmd_copy_file = ["cp", new_file_path, wd_current]
        run_cmd(cmd_copy_file)


if __name__ == "__main__":
    main()
