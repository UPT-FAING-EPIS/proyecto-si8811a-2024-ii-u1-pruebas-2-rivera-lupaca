import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:flutter_application_1/main.dart';

void main() {
  testWidgets('Login button is present and functional', (WidgetTester tester) async {
    // Construir el widget de la pantalla de inicio de sesión.
    await tester.pumpWidget(const MaterialApp(home: LoginScreen()));

    // Verificar que el botón de login esté presente.
    expect(find.text('Login with Microsoft'), findsOneWidget);

    // Simular un tap en el botón.
    await tester.tap(find.text('Login with Microsoft'));

    // Esperar que se ejecute la acción de tap.
    await tester.pump();

    // Aquí podrías agregar verificaciones adicionales si la acción del botón cambia algo en la UI.
    // Por ahora solo imprime un mensaje para confirmar el clic.
    print('El botón de login fue presionado correctamente.');
  });
}
