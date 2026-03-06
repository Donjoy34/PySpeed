import * as vscode from 'vscode';
import * as fs from 'fs';

export function activate(context) {

    const decoration = vscode.window.createTextEditorDecorationType({
        after: {
            color: "#888888",
            margin: "0 0 0 20px"
        }
    });

    function showProfile() {

        const editor = vscode.window.activeTextEditor;
        if (!editor) return;

        const profile = JSON.parse(
            fs.readFileSync("pyspeed_profile.json", "utf8")
        );

        const decorations = [];

        const text = editor.document.getText();
        const lines = text.split("\n");

        lines.forEach((line, i) => {

            const match = line.match(/def\s+(\w+)/);

            if (match) {

                const func = match[1];

                if (profile[func]) {

                    const data = profile[func];

                    const label =
                        ` ⏱ ${data.time.toFixed(4)}s | 🧠 ${data.memory.toFixed(2)}KB`;

                    decorations.push({
                        range: new vscode.Range(i, line.length, i, line.length),
                        renderOptions: {
                            after: { contentText: label }
                        }
                    });
                }
            }

        });

        editor.setDecorations(decoration, decorations);
    }

    vscode.workspace.onDidSaveTextDocument(showProfile);

}