import 'package:go_router/go_router.dart';
import 'package:flutter/material.dart';

class StudentHomeScreen extends StatelessWidget {
  const StudentHomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final items = [
      ('Raise Complaint', Icons.add_circle),
      ('My Complaints', Icons.list_alt),
      ('Notifications', Icons.notifications),
      ('Profile', Icons.person),
    ];

    return Scaffold(
      
      floatingActionButton: FloatingActionButton( 
        onPressed: () { 
          context.push('/admin-dashboard'); 
          }, 
          child: const Icon(Icons.admin_panel_settings), 
        ),
      appBar: AppBar(
        title: const Text('FixAI'),
        centerTitle: true,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: GridView.builder(
          itemCount: items.length,
          gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
            crossAxisCount: 2,
            crossAxisSpacing: 12,
            mainAxisSpacing: 12,
            childAspectRatio:1.15,
          ),
          itemBuilder: (context, index) {
            final item = items[index];

            return Card(
              elevation: 2,
              child: InkWell(
                borderRadius: BorderRadius.circular(16),
                onTap: () { 
                  if (item.$1 == 'Raise Complaint') { 
                    context.push('/raise-complaint'); 
                  } else if (item.$1 == 'My Complaints') { 
                    context.push('/my-complaints'); 
                  } else if (item.$1 == 'Notifications') { 
                    context.push('/notifications'); 
                  } else if (item.$1 == 'Profile') { 
                    context.push('/profile'); 
                  } 
                },
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Icon(item.$2, size: 32),
                    const SizedBox(height: 12),
                    Text(
                      item.$1,
                      textAlign: TextAlign.center,
                      style: const TextStyle(
                        fontSize:14,
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                  ],
                ),
              ),
            );
          },
        ),
      ),
    );
  }
}