import 'package:go_router/go_router.dart';
import 'package:flutter/material.dart';

class RaiseComplaintScreen extends StatelessWidget {
  const RaiseComplaintScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Raise Complaint'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            TextField(
              decoration: InputDecoration(
                labelText: 'Title',
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 16),

            TextField(
              maxLines: 5,
              decoration: InputDecoration(
                labelText: 'Describe the issue',
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 16),

            DropdownButtonFormField<String>(
              items: const [
                DropdownMenuItem(value: 'Electrical', child: Text('Electrical')),
                DropdownMenuItem(value: 'Water', child: Text('Water')),
                DropdownMenuItem(value: 'Cleaning', child: Text('Cleaning')),
                DropdownMenuItem(value: 'Internet', child: Text('Internet')),
              ],
              onChanged: (_) {},
              decoration: const InputDecoration(
                labelText: 'Category',
                border: OutlineInputBorder(),
              ),
            ),

            const SizedBox(height: 24),

            SizedBox(
              width: double.infinity,
              height: 52,
              child: FilledButton(
                onPressed: () { 
                  context.push('/ai-review'); 
                },
                child: const Text('Submit Complaint'),
              ),
            ),
          ],
        ),
      ),
    );
  }
}