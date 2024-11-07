import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';

export default function App() {
    const [length, setLength] = useState("");
    const [password, setPassword] = useState("");

    const generatePassword = () => {
        const chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()";
        let result = "";
        for (let i = 0; i < parseInt(length); i++) {
            result += chars.charAt(Math.floor(Math.random() * chars.length));
        }
        setPassword(result);
    };

    return (
        <View style={styles.container}>
            <Text>Password Generator</Text>
            <TextInput 
                style={styles.input} 
                placeholder="Password Length"
                keyboardType="numeric"
                onChangeText={(text) => setLength(text)}
            />
            <Button title="Generate Password" onPress={generatePassword} />
            <Text style={styles.result}>{password}</Text>
        </View>
    );
}

const styles = StyleSheet.create({
    container: { flex: 1, justifyContent: 'center', alignItems: 'center' },
    input: { borderWidth: 1, padding: 10, margin: 10, width: 200 },
    result: { fontSize: 20, marginTop: 20 }
});
