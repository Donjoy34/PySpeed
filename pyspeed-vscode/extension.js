const vscode = require('vscode');
const fs = require('fs');
const path = require('path');

function activate(context) {

    const decoration = vscode.window.createTextEditorDecorationType({
        after: {
            color: "#888888",
            margin: "0 0 0 20px"
        }
    });

    function getProfilePath() {
        const folder = vscode.workspace.workspaceFolders && vscode.workspace.workspaceFolders[0];
        if (!folder) {
            return null;
        }

        return path.join(folder.uri.fsPath, 'pyspeed_profile.json');
    }

    function showProfile() {

        const editor = vscode.window.activeTextEditor;
        if (!editor) return;

        if (editor.document.languageId !== 'python') {
            return;
        }

        const profilePath = getProfilePath();
        if (!profilePath || !fs.existsSync(profilePath)) {
            editor.setDecorations(decoration, []);
            return;
        }

        let profile;
        try {
            profile = JSON.parse(fs.readFileSync(profilePath, 'utf8'));
        } catch {
            editor.setDecorations(decoration, []);
            return;
        }

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

    context.subscriptions.push(vscode.workspace.onDidSaveTextDocument(() => {
        showProfile();
    }));

    context.subscriptions.push(vscode.window.onDidChangeActiveTextEditor(() => {
        showProfile();
    }));

    context.subscriptions.push(decoration);

    showProfile();

}

module.exports = {
    activate
};