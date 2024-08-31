import 'package:flutter_test/flutter_test.dart';
import 'package:integration_test/integration_test.dart';
import 'package:flutter_application_1/main.dart';

void main() {
  IntegrationTestWidgetsFlutterBinding.ensureInitialized();

  testWidgets('Test de flujo completo de login', (WidgetTester tester) async {
    // Construir la aplicación completa.
    await tester.pumpWidget(const MyApp());

    // Verificar que el texto "Login with Microsoft" esté presente.
    expect(find.text('Login with Microsoft'), findsOneWidget);

    // Simular un tap en el botón de login.
    await tester.tap(find.text('Login with Microsoft'));

    // Esperar que se ejecuten todas las animaciones y transiciones.
    await tester.pumpAndSettle();

    // Aquí podrías verificar que la pantalla haya cambiado o que se haya realizado alguna acción.
    print('Flujo de login probado con éxito.');
  });
}
