// screens/Dashboard.js
import React, { useEffect, useState } from 'react';
import { View, Text, TextInput, FlatList, Image, StyleSheet, TouchableOpacity } from 'react-native';
import { useNavigation } from '@react-navigation/native';

  
export default function Dashboard() {
  const [products, setProducts] = useState([]);
  const [search, setSearch] = useState('');
  const navigation = useNavigation();

  useEffect(() => {
    fetch('http://192.168.5.235:3000/api/products') // Replace with your API URL
      .then((response) => response.json())
      .then((data) => setProducts(data))
      .catch((error) => console.error('Error fetching products:', error));
  }, []);

  const filteredProducts = products.filter((product) =>
    product.name.toLowerCase().includes(search.toLowerCase())
  );

  const renderProduct = ({ item }) => (
    <View style={styles.productCard}>
      <Image source={{ uri: item.image }} style={styles.productImage} />
      <Text style={styles.productName}>{item.name}</Text>
      <Text style={styles.productPrice}>Price: NPR {item.price}</Text>
      <Text style={styles.productQuantity}>Available: {item.total_quantity}</Text>
    </View>
  );

  return (
    <View style={styles.container}>
      <TextInput
        style={styles.searchBar}
        placeholder="\Search products...\"
        value={search}
        onChangeText={(text) => setSearch(text)}
      />
      <FlatList
        data={filteredProducts}
        keyExtractor={(item) => item._id}
        renderItem={renderProduct}
        ListEmptyComponent={<Text>No products found.</Text>}
      />
      <TouchableOpacity
        style={styles.scanButton}
        onPress={() => navigation.navigate('ScanToPay')}
      >
        <Text style={styles.buttonText}>Scan to Pay</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 10, backgroundColor: '#f8f9fa' },
  searchBar: { padding: 10, borderColor: '#ddd', borderWidth: 1, marginBottom: 10 },
  productCard: { backgroundColor: '#fff', padding: 15, borderRadius: 10, marginBottom: 10 },
  productImage: { width: '100%', height: 150, borderRadius: 10 },
  productName: { fontSize: 18, fontWeight: 'bold', marginVertical: 5 },
  productPrice: { fontSize: 16, color: '#28a745' },
  productQuantity: { fontSize: 14, color: '#6c757d' },
  scanButton: { marginTop: 20, padding: 15, backgroundColor: '#007bff', borderRadius: 10 },
  buttonText: { color: '#fff', textAlign: 'center', fontSize: 16, fontWeight: 'bold' },
});
