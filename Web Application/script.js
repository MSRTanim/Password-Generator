function generatePassword() {
    const length = document.getElementById("length").value;
    const chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()";
    let password = "";
    
    if (length < 6) {
        alert("Password length should be at least 6.");
        return;
    }

    for (let i = 0; i < length; i++) {
        password += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    
    document.getElementById("result").innerText = password;
}

function copyToClipboard() {
    const password = document.getElementById("result").innerText;
    if (!password) {
        alert("Please generate a password first.");
        return;
    }

    navigator.clipboard.writeText(password).then(() => {
        alert("Password copied to clipboard!");
    });
}
