package e_wallet.wallet_service.entity;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;

import java.math.BigDecimal;
import java.time.Instant;
import java.util.UUID;

@Entity
@Table(name = "wallet")
@AllArgsConstructor
@NoArgsConstructor
@Data
public class Wallet {
    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    @Column(name = "wallet_id")
    private UUID wallet_id;

    @Column(name = "user_id")
    private UUID user_id;

    @Column(name = "balance")
    private BigDecimal balance;

    @Column(name = "status")
    private Integer status;

    @CreationTimestamp
    @Column(name = "created_at")
    private Instant created_at;

    @UpdateTimestamp
    @Column(name = "updated_at")
    private Instant update_at;
}
