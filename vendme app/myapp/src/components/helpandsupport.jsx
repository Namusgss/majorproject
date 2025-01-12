// screens/HelpAndSupport.js
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default function HelpAndSupport() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Help & Support</Text>
      <Text style={styles.content}>
        For any issues or queries, please contact us at support@example.com or call +977-1234567890.
      </Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', alignItems: 'center', padding: 20 },
  title: { fontSize: 22, fontWeight: 'bold', marginBottom: 10 },
  content: { fontSize: 16, textAlign: 'center', lineHeight: 24 },
});
